//
//  ContentView.swift
//  ApartmentsApp
//
//  Created by Kevin Furjan on 24.05.2021.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        LoginView()
            .preferredColorScheme(/*@START_MENU_TOKEN@*/.dark/*@END_MENU_TOKEN@*/)
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
