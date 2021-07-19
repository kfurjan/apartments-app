//
//  DaoRepositoryFactory.swift
//  ApartmentsAppMobile
//
//  Created by Ericsson on 18.07.2021.
//

class DaoRepositoryFactory {
    static func getRepository() -> DaoRepository {
        return DaoHandler()
    }
}
