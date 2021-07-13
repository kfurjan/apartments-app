//
//  NetworkError.swift
//  ApartmentsAppMobile
//
//  Created by Kevin Furjan on 13.07.2021.
//

import Foundation

enum NetworkError: Error, CustomStringConvertible {
    case customError(message: String)
    case accessKeyError
    case generalErrorLogin
    case generalErrorRegister
    case incorrectCredentials
    case nonMatchingPasswords

    var description: String {
        switch self {
        case .accessKeyError: return "Unable to retrieve access key"
        case .generalErrorLogin: return "Error while logging in"
        case .generalErrorRegister: return "Error while registering new user"
        case .incorrectCredentials: return "Incorrect email or password"
        case .nonMatchingPasswords: return "Passwords do not match"
        case .customError(let message): return message
        }
    }
}
