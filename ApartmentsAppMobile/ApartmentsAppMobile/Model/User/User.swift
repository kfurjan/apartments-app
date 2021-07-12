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
    var accessToken: String
    var passwordDigest: String

    private enum CodingKeys: String, CodingKey {
        case idUser = "id"
        case email = "email"
        case role = "role"
        case accessToken = "access_token"
        case passwordDigest = "password_digest"
    }

    init() {
        idUser = 0
        email = ""
        role = UserRole.guest
        accessToken = ""
        passwordDigest = ""
    }
}
