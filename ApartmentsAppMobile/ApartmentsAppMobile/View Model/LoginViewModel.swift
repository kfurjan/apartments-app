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

    private var _apiRepository = ApiRepositoryFactory.getRepository()

    @Published var formModel: FormModel
    @Published var didErrorHappen = false
    @Published var errorMessage = ""

    init(isPreview: Bool = false) {
        formModel = FormModel(
            formState: isPreview ? .signUpForm : .loginForm,
            loginSuccessful: false,
            credentials: Credentials(email: "", password: "", repeatedPassword: "", isGuest: false, isRenter: false)
        )
    }

    func setFormState(formState: FormState) {
        self.formModel.formState = formState
    }

    func getFormState() -> FormState {
        formModel.formState
    }

    func cleanForm() {
        formModel.credentials.email = ""
        formModel.credentials.password = ""
        formModel.credentials.repeatedPassword = ""
    }

    func cleanView() {
        formModel.credentials.email = ""
        formModel.credentials.password = ""
        formModel.credentials.repeatedPassword = ""
        didErrorHappen = false
        errorMessage = ""
    }

    func loginUser(credentials: Credentials) {
        _apiRepository.loginUser(credentials: credentials) { result in
            switch result {
            case .success(let accessToken):
                self.formModel.loginSuccessful = true
                UserDefaults.standard.set(accessToken, forKey: accessTokenKey)
                UserDefaults.standard.set(self.formModel.loginSuccessful, forKey: isUserLoggedInKey)

            case .failure(let error):
                self.cleanForm()
                self.didErrorHappen = true
                self.errorMessage = error.description
            }
        }
    }

    func registerUser(credentials: Credentials) {
        _apiRepository.registerUser(credentials: credentials) { result in
            switch result {
            case .success(let accessToken):
                self.formModel.loginSuccessful = true
                UserDefaults.standard.set(accessToken, forKey: accessTokenKey)
                UserDefaults.standard.set(self.formModel.loginSuccessful, forKey: isUserLoggedInKey)

            case .failure(let error):
                self.cleanForm()
                self.didErrorHappen = true
                self.errorMessage = error.description
            }
        }
    }
}
