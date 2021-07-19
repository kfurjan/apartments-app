//
//  AppViewModel.swift
//  ApartmentsAppMobile
//
//  Created by Kevin Furjan on 11.07.2021.
//

import Combine
import Foundation

final class AppViewModel: ObservableObject {

    private let _apiRepository = ApiRepositoryFactory.getRepository()

    @Published var user = User()
    @Published var isUserLoggedIn = false
    @Published var isUserLoggedOut = false

    init(isPreview: Bool = false) {
        if isPreview {
            isUserLoggedIn = true
            user = {
                let user = User()
                user.role = UserRole.renter
                user.email = "kfurjan@gmail.com"
                return user
            }()
        } else {
            initUser()
        }
    }

    func fetchUserData() {
        initUser()
    }

    private func initUser() {
        guard let accessToken = UserDefaults.standard.string(forKey: accessTokenKey) else {
            user = User()
            return
        }

        isUserLoggedIn = UserDefaults.standard.bool(forKey: isUserLoggedInKey)
        if isUserLoggedIn {
            isUserLoggedOut = false
            _apiRepository.getUser(accessToken: accessToken) { result in
                switch result {
                case .success(let user):
                    self.user = user
                case .failure(let error):
                    print(error) // TODO: do something smarter with this
                }
            }
        }
    }

    func logOutUser() {
        isUserLoggedOut = true
        isUserLoggedIn = false

        UserDefaults.standard.set(isUserLoggedIn, forKey: isUserLoggedInKey)
        UserDefaults.standard.set(nil, forKey: accessTokenKey)
    }
}
