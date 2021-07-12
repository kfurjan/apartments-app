//
//  LoginViewModel.swift
//  ApartmentsApp
//
//  Created by Kevin Furjan on 24.05.2021.
//

import Alamofire
import Combine
import Foundation
import SwiftyJSON

final class LoginViewModel: ObservableObject {

    @Published var formModel: FormModel
    @Published var didErrorHappen = false
    @Published var errorMessage = ""

    init(isPreview: Bool = false) {
        formModel = FormModel(
            email: "",
            isGuest: true,
            isRenter: false,
            password: "",
            loginSuccessful: false,
            repeatedPassword: "",
            formState: isPreview ? .signUpForm : .loginForm
        )
    }

    func setFormState(formState: FormState) {
        self.formModel.formState = formState
    }

    func getFormState() -> FormState {
        formModel.formState
    }

    func cleanForm() {
        formModel.email = ""
        formModel.password = ""
        formModel.repeatedPassword = ""
    }

    func cleanView() {
        formModel.email = ""
        formModel.password = ""
        formModel.repeatedPassword = ""
        didErrorHappen = false
        errorMessage = ""
    }

    func loginUser(formModel: FormModel) { // TODO: repository pattern
        didErrorHappen = false
        errorMessage = ""

        let parameters = ["email": formModel.email, "password_digest": formModel.password]
        AF.request(
            ApiConstants.loginApiEndpoint,
            method: .post,
            parameters: parameters,
            encoding: JSONEncoding.default
        ).responseJSON { response in
            switch response.result {
            case .success(let data):
                guard case (200 ... 299) = response.response!.statusCode else {
                    self.cleanForm()
                    self.errorMessage = JSON(data)["errors"][0].string ?? "Error occured"
                    self.didErrorHappen = true
                    return
                }

                guard let accessToken = JSON(data)["access_token"].string else {
                    self.cleanForm()
                    self.errorMessage = "Unable to retrieve access key"
                    self.didErrorHappen = true
                    return
                }

                self.formModel.loginSuccessful = true
                UserDefaults.standard.set(accessToken, forKey: accessTokenKey)
                UserDefaults.standard.set(self.formModel.loginSuccessful, forKey: isUserLoggedInKey)
            case .failure(let error):
                self.didErrorHappen = true
                self.errorMessage = error.localizedDescription
            }
        }
    }

    func registerUser(formModel: FormModel) { // TODO: repository pattern
        didErrorHappen = false
        errorMessage = ""

        if formModel.password != formModel.repeatedPassword {
            didErrorHappen = false
            errorMessage = "Passwords do not match"
        } else {
            let parameters = [
                "email": formModel.email,
                "password_digest": formModel.password,
                "role": formModel.isGuest ? UserRole.guest.rawValue : UserRole.renter.rawValue
            ]
            AF.request(
                ApiConstants.userApiEndpoint,
                method: .post,
                parameters: parameters,
                encoding: JSONEncoding.default
            ).responseJSON { response in
                switch response.result {
                case .success(let data):
                    guard case (200 ... 299) = response.response!.statusCode else {
                        self.cleanForm()
                        self.errorMessage = JSON(data)["errors"][0].string ?? "Error occured"
                        self.didErrorHappen = true
                        return
                    }

                    guard let accessToken = JSON(data)["access_token"].string else {
                        self.cleanForm()
                        self.errorMessage = "Unable to retrieve access key"
                        self.didErrorHappen = true
                        return
                    }

                    self.formModel.loginSuccessful = true
                    UserDefaults.standard.set(accessToken, forKey: accessTokenKey)
                    UserDefaults.standard.set(self.formModel.loginSuccessful, forKey: isUserLoggedInKey)
                case .failure(let error):
                    self.didErrorHappen = true
                    self.errorMessage = error.localizedDescription
                }
            }
        }
    }
}
