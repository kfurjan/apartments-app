//
//  DaoRepository.swift
//  ApartmentsAppMobile
//
//  Created by Kevin Furjan on 18.07.2021.
//

protocol DaoRepository {

    // MARK: Apartments CRUD operations
    func createApartments(apartments: [Apartment])
    func retrieveApartments() -> [Apartment]
}
