//
//  RestApiHandler.swift
//  ApartmentsAppMobile
//
//  Created by Kevin Furjan on 13.07.2021.
//

import Alamofire
import Foundation
import RealmSwift
import SwiftyJSON

final class RestApiHandler: ApiRepository {

    // MARK: User CRUD operations
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

    func getUser(
        accessToken: String,
        completionHandler: @escaping (Swift.Result<User, NetworkError>) -> Void
    ) {
        if accessToken == "" { completionHandler(.failure(.accessKeyError)) }

        let headers: HTTPHeaders = [.authorization(bearerToken: accessToken)]
        AF.request(
            ApiConstants.userApiEndpoint,
            method: .get,
            encoding: JSONEncoding.default,
            headers: headers
        )
        .validate(statusCode: 200..<300)
        .responseDecodable(of: User.self) { response in
            switch response.result {
            case .success(let user):
                completionHandler(.success(user))
            case .failure(let error):
                completionHandler(.failure(.customError(message: error.localizedDescription)))
            }
        }
    }

    // MARK: Apartments CRUD operations
    func getAllApartments(
        completionHandler: @escaping (Swift.Result<[Apartment], NetworkError>) -> Void
    ) {
        AF.request(
            ApiConstants.apartmentsApiEndpoint,
            method: .get,
            encoding: JSONEncoding.default
        )
        .validate(statusCode: 200..<300)
        .responseJSON { response in
            switch response.result {
            case .success(let jsonData):
                var apartments: [Apartment] = []

                guard let apartmentJsonList = JSON(jsonData).array else {
                    completionHandler(.success(apartments))
                    return
                }

                for apartmentJsonData in apartmentJsonList {
                    let realmimages = List<String>()
                    realmimages.append(
                        objectsIn: apartmentJsonData["images"]["imageslist"].arrayObject as? [String] ?? [String]()
                    )

                    apartments.append(Apartment(
                        id: apartmentJsonData["id"].int ?? 0,
                        title: apartmentJsonData["title"].string ?? "",
                        city: apartmentJsonData["city"].string ?? "",
                        address: apartmentJsonData["address"].string ?? "",
                        postalCode: apartmentJsonData["postal_code"].string ?? "",
                        apartmentDesc: apartmentJsonData["description"].string ?? "",
                        pricePerNight: apartmentJsonData["price_per_night"].double ?? 0.0,
                        available: apartmentJsonData["available"].bool ?? false,
                        availableFrom: Date.parse(apartmentJsonData["availability_start_date"].string ?? "") ?? Date(),
                        availableTo: Date.parse(apartmentJsonData["availability_end_date"].string ?? "") ?? Date(),
                        latitude: apartmentJsonData["latitude"].double ?? 0.0,
                        longitude: apartmentJsonData["longitude"].double ?? 0.0,
                        images: realmimages
                    ))
                }

                completionHandler(.success(apartments))
            case .failure(let error):
                completionHandler(.failure(.customError(message: error.localizedDescription)))
            }
        }
    }
}
