//
//  DaoHandler.swift
//  ApartmentsAppMobile
//
//  Created by Kevin Furjan on 18.07.2021.
//

import Foundation
import RealmSwift

final class DaoHandler: DaoRepository {

    let localRealm = try! Realm()

    // MARK: Apartments CRUD operations
    func createApartments(apartments: [Apartment]) {
        try! localRealm.write {
            localRealm.deleteAll()
            localRealm.add(apartments)
        }
    }

    func retrieveApartments() -> [Apartment] {
        Array(localRealm.objects(Apartment.self))
    }
}
