//
//  ApiRepository.swift
//  ApartmentsAppMobile
//
//  Created by Kevin Furjan on 13.07.2021.
//

protocol ApiRepository {
    func loginUser(
        credentials: Credentials,
        completionHandler: @escaping (Swift.Result<String, NetworkError>) -> Void
    )
    func registerUser(
        credentials: Credentials,
        completionHandler: @escaping (Swift.Result<String, NetworkError>) -> Void
    )
}
