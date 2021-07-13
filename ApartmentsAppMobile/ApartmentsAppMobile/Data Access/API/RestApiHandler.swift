//
//  RestApiHandler.swift
//  ApartmentsAppMobile
//
//  Created by Kevin Furjan on 13.07.2021.
//

import Alamofire
import Foundation
import SwiftyJSON

final class RestApiHandler: ApiRepository {

    func loginUser(
        credentials: Credentials,
        completionHandler: @escaping (Result<String, NetworkError>) -> Void
    ) {
        if credentials.email == "" || credentials.password == "" {
            completionHandler(.failure(.incorrectCredentials))
        }

        let parameters = ["email": credentials.email, "password_digest": credentials.password]
        AF.request(
            ApiConstants.loginApiEndpoint,
            method: .post,
            parameters: parameters,
            encoding: JSONEncoding.default
        )
        .validate(statusCode: 200..<300)
        .responseJSON { response in
            switch response.result {
            case .success(let data):
                guard let accessToken = JSON(data)["access_token"].string else {
                    completionHandler(.failure(.accessKeyError))
                    return
                }

                completionHandler(.success(accessToken))

            case .failure(_):
                completionHandler(.failure(.generalErrorLogin))
            }
        }
    }

    func registerUser(
        credentials: Credentials,
        completionHandler: @escaping (Result<String, NetworkError>) -> Void
    ) {
        if credentials.email == "" || credentials.password == "" || credentials.repeatedPassword == "" {
            completionHandler(.failure(.incorrectCredentials))
        }
        if credentials.password != credentials.repeatedPassword { completionHandler(.failure(.nonMatchingPasswords)) }

        let parameters = [
            "email": credentials.email,
            "password_digest": credentials.password,
            "role": credentials.isGuest ? UserRole.guest.rawValue : UserRole.renter.rawValue
        ]
        AF.request(
            ApiConstants.userApiEndpoint,
            method: .post,
            parameters: parameters,
            encoding: JSONEncoding.default
        )
        .validate(statusCode: 200..<300)
        .responseJSON { response in
            switch response.result {
            case .success(let data):
                guard let accessToken = JSON(data)["access_token"].string else {
                    completionHandler(.failure(.accessKeyError))
                    return
                }

                completionHandler(.success(accessToken))

            case .failure(_):
                completionHandler(.failure(.generalErrorRegister))
            }
        }
    }
}
