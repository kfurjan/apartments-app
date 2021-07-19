//
//  User.swift
//  ApartmentsApp
//
//  Created by Kevin Furjan on 24.05.2021.
//

import Foundation

class User: Codable {
    var id: Int
    var email: String
    var role: UserRole
    var renterId: Int?
    var guestId: Int?

    private enum CodingKeys: String, CodingKey {
        case id = "id"
        case email = "email"
        case role = "role"
        case renterId = "renter_id"
        case guestId = "guest_id"
    }

    init() {
        id = 0
        email = ""
        role = UserRole.guest
    }
}
