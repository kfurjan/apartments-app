//
//  ApiRepository.swift
//  ApartmentsAppMobile
//
//  Created by Kevin Furjan on 13.07.2021.
//

protocol ApiRepository {

    // MARK: User CRUD operations
    func loginUser(
        credentials: Credentials,
        completionHandler: @escaping (Swift.Result<String, NetworkError>) -> Void
    )
    func registerUser(
        credentials: Credentials,
        completionHandler: @escaping (Swift.Result<String, NetworkError>) -> Void
    )
    func getUser(
        accessToken: String,
        completionHandler: @escaping (Swift.Result<User, NetworkError>) -> Void
    )

    // MARK: Apartments CRUD operations
    func getAllApartments(
        completionHandler: @escaping (Swift.Result<[Apartment], NetworkError>) -> Void
    )
}
