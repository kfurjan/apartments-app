//
//  ApartmentsSearchView.swift
//  ApartmentsAppMobile
//
//  Created by Kevin Furjan on 04.06.2021.
//

import SwiftUI

struct ApartmentsSearchView: View {
    @StateObject private var viewModel = ApartmentsViewModel()

    var body: some View {
        NavigationView {
            VStack {
                SearchBar(state: $viewModel.searchBarState)
                    .padding()
                    .onChange(of: viewModel.searchBarState.text) { _ in
                        viewModel.filterApartments()
                    }

                HStack {
                    Spacer()
                    Button(action: {
                        viewModel.apartmentsViewState.sortDescending.toggle()

                        viewModel.sortApartmentsAscending(
                            viewModel.apartmentsViewState.sortDescending
                        )
                    }, label: {
                        Image(systemName: sortIcon)
                            .font(.headline)
                            .foregroundColor(Color(secondaryColor))
                    })
                }.padding()

                ScrollView {
                    ForEach(viewModel.apartmentsViewState.apartments, id: \.id) { apartment in
                        NavigationLink(destination: ApartmentDetailView(apartment: apartment)) {
                            ApartmentPreview(apartment: apartment)
                        }
                        .buttonStyle(PlainButtonStyle())
                    }
                }
            }
            .navigationTitle(apartments)
            .navigationBarItems(trailing:
                Button(action: {
                    viewModel.apartmentsViewState.isSheetPresented.toggle()
                }, label: {
                    Image(systemName: filterIcon)
                        .font(.title)
                        .foregroundColor(Color(secondaryColor))
                })
            )
            .sheet(isPresented: $viewModel.apartmentsViewState.isSheetPresented) {
                VStack {
                    HStack {
                        Text(filters)
                            .font(.title)
                            .fontWeight(.bold)
                        Spacer()
                    }.padding()

                    Picker(filters, selection: $viewModel.apartmentsViewState.selectedFilter) {
                        ForEach(viewModel.apartmentsViewState.filterOptions, id: \.self) { filter in
                            Text(filter)
                        }
                    }
                }
            }
            .background(Color(primaryColor).edgesIgnoringSafeArea(.all))
        }
        .onAppear {
            viewModel.fetchApartments()
        }
    }
}

struct ApartmentsSearchView_Previews: PreviewProvider {
    static var previews: some View {
        ApartmentsSearchView()
            .preferredColorScheme(.dark)
    }
}
