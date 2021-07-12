//
//  ContentView.swift
//  ApartmentsApp
//
//  Created by Kevin Furjan on 24.05.2021.
//

import SwiftUI

struct ContentView: View {

    @StateObject var appViewModel = AppViewModel()

    var body: some View {
        VStack {
            if appViewModel.isUserLoggedIn {
                ApartmentsSearchView()
                       .preferredColorScheme(.dark)
            } else {
                LoginView()
                    .preferredColorScheme(/*@START_MENU_TOKEN@*/.dark/*@END_MENU_TOKEN@*/)
                    .navigate(
                        to: ApartmentsSearchView()
                                .preferredColorScheme(.dark),
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
            ContentView()
                .environmentObject(AppViewModel())
        }
    }
}
