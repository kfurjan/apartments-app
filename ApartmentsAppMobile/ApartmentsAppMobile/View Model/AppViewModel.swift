//
//  AppViewModel.swift
//  ApartmentsAppMobile
//
//  Created by Kevin Furjan on 11.07.2021.
//

import Combine
import Foundation

final class AppViewModel: ObservableObject {

    @Published var user = User()
    @Published var isUserLoggedIn = false

    init() {
        initUser()
    }

    private func initUser() {
        isUserLoggedIn = UserDefaults.standard.bool(forKey: isUserLoggedInKey)
        guard let accessToken = UserDefaults.standard.string(forKey: accessTokenKey) else {
            user = User()
            return
        }

        user = { // TODO: implement repository which calls REST API
            let user = User()
            user.accessToken = accessToken
            return user
        }()
    }

    func fetchData() {
        initUser()
    }
}
