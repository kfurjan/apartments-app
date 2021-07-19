//
//  ContentView.swift
//  ApartmentsApp
//
//  Created by Kevin Furjan on 24.05.2021.
//

import SwiftUI

struct HomeView: View {
    var body: some View {
        TabView {
            ApartmentsSearchView()
                .preferredColorScheme(.dark)
                .tabItem { Label(apartments, systemImage: houseIcon) }

            UserView()
                .preferredColorScheme(.dark)
                .tabItem { Label(user, systemImage: personIcon) }
        }
    }
}

struct ContentView: View {

    @StateObject var appViewModel = AppViewModel()

    var body: some View {
        VStack {
            if appViewModel.isUserLoggedIn {
                HomeView()
            } else {
                LoginView()
                    .preferredColorScheme(/*@START_MENU_TOKEN@*/.dark/*@END_MENU_TOKEN@*/)
                    .navigate(
                        to: HomeView(),
                        when: $appViewModel.isUserLoggedIn
                    )
            }
        }
        .environmentObject(appViewModel)
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        Group {
            HomeView()
                .environmentObject(AppViewModel(isPreview: true))

            ContentView()
                .environmentObject(AppViewModel())
        }
    }
}
