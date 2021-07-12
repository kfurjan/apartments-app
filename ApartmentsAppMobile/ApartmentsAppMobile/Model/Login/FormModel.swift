//
//  LoginFormModel.swift
//  ApartmentsAppMobile
//
//  Created by Kevin Furjan on 26.05.2021.
//

struct FormModel {
    var email: String
    var isGuest: Bool
    var isRenter: Bool
    var password: String
    var loginSuccessful: Bool
    var repeatedPassword: String
    var formState: FormState
}
