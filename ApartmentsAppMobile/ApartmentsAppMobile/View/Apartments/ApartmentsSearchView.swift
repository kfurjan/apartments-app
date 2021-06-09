//
//  ApartmentsSearchView.swift
//  ApartmentsAppMobile
//
//  Created by Kevin Furjan on 04.06.2021.
//

import SwiftUI

struct ApartmentsSearchView: View {
    @State private var sortDescending = false
    @State private var isSheetPresented = false
    @State private var selectedFilter = "City"
    let filterOptions = ["City", "Price", "Rating", "Available"]

    var body: some View {
        NavigationView {
            VStack {
                SearchBar()
                    .padding()

                HStack {
                    Spacer()
                    Button(action: {
                        self.sortDescending.toggle()
                    }, label: {
                        Image(systemName: searchIcon)
                            .font(.headline)
                            .foregroundColor(Color(secondaryColor))
                    })
                }.padding()

                ScrollView {
                    ForEach(apartmentsList, id: \.id) { apartment in
                        ApartmentPreview(apartment: apartment)
                    }
                }
            }
            .navigationTitle(apartments)
            .navigationBarItems(trailing:
                Button(action: {
                    self.isSheetPresented.toggle()
                }, label: {
                    Image(systemName: filterIcon)
                        .font(.title)
                        .foregroundColor(Color(secondaryColor))
                })
            )
            .sheet(isPresented: $isSheetPresented) {
                VStack {
                    HStack {
                        Text(filters)
                            .font(.title)
                            .fontWeight(.bold)
                        Spacer()
                    }.padding()

                    Picker(filters, selection: $selectedFilter) {
                        ForEach(filterOptions, id: \.self) { filter in
                            Text(filter)
                        }
                    }
                }
            }
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
