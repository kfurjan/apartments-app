//
//  ApartmentsSearchView.swift
//  ApartmentsAppMobile
//
//  Created by Kevin Furjan on 04.06.2021.
//

import SwiftUI

struct ApartmentsSearchView: View {
    var body: some View {
        NavigationView {
            VStack {
                SearchBar()
                    .padding()

                ScrollView {
                    ForEach(apartmentsList, id: \.id) { apartment in
                        ApartmentPreview(apartment: apartment)
                    }
                }
            }
            .navigationTitle(apartments)
            .background(Color(primaryColor).edgesIgnoringSafeArea(.all))
        }
    }
}

struct ApartmentsSearchView_Previews: PreviewProvider {
    static var previews: some View {
        ApartmentsSearchView()
            .preferredColorScheme(.dark)
    }
}
