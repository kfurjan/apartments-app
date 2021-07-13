//
//  User.swift
//  ApartmentsApp
//
//  Created by Kevin Furjan on 24.05.2021.
//

import Combine
import Foundation

class User: Codable {
    var idUser: Int
    var email: String
    var role: UserRole
    var password: String
    var accessToken: String

    private enum CodingKeys: String, CodingKey {
        case idUser = "id"
        case email = "email"
        case password = "password_digest"
        case role = "role"
        case accessToken = "access_token"
    }

    init() {
        idUser = 0
        email = ""
        role = UserRole.guest
        accessToken = ""
        password = ""
    }
}
