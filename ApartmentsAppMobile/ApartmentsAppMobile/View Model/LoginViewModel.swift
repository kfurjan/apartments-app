//
//  LoginViewModel.swift
//  ApartmentsApp
//
//  Created by Kevin Furjan on 24.05.2021.
//

import Combine

class LoginViewModel: ObservableObject {

    @Published var formModel: FormModel

    init(isPreview: Bool = false) {
        formModel = FormModel(
            email: "",
            password: "",
            repeatPassword: "",
            formState: isPreview ? .signUpForm : .loginForm
        )
    }

    func setFormState(formState: FormState) {
        self.formModel.formState = formState
    }

    func getFormState() -> FormState {
        formModel.formState
    }

    func cleanUp() {
        formModel.email = ""
        formModel.password = ""
        formModel.repeatPassword = ""
    }
}
