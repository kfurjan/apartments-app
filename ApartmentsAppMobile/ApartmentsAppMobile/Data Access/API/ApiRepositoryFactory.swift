//
//  ApiRepositoryFactory.swift
//  ApartmentsAppMobile
//
//  Created by Kevin Furjan on 13.07.2021.
//

class ApiRepositoryFactory {
    static func getRepository() -> ApiRepository {
        return RestApiHandler()
    }
}
