//
//  ApartmentsViewModel.swift
//  ApartmentsAppMobile
//
//  Created by Kevin Furjan on 22.06.2021.
//

import Combine
import Foundation

enum FilterOptions: String, CaseIterable {
    case city = "City"
    case price = "Price"
    case rating = "Rating"
}

final class ApartmentsViewModel: ObservableObject {

    @Published var searchBarState = SearchBarState()
    @Published var apartmentsViewState: ApartmentViewState

    init() {
        apartmentsViewState = ApartmentViewState(
            sortDescending: false,
            isSheetPresented: false,
            selectedFilter: FilterOptions.price.rawValue,
            filterOptions: FilterOptions.allCases.map { $0.rawValue },
            apartments: apartmentsList
        )
    }

    func filterApartments() {
        if searchBarState.text == "" {
            apartmentsViewState.apartments = apartmentsList
        } else {
            apartmentsViewState.apartments = apartmentsViewState.apartments.filter {
                $0.tile.lowercased().contains(searchBarState.text.lowercased())
                || $0.city.lowercased().contains(searchBarState.text.lowercased())
            }
        }
    }

    func sortApartmentsAscending(_ sortAscending: Bool) {
        switch apartmentsViewState.selectedFilter {
        case FilterOptions.city.rawValue:
            apartmentsViewState.apartments = apartmentsViewState.apartments.sorted(
                by: { sortAscending ? $0.city < $1.city : $0.city > $1.city }
            )
        case FilterOptions.price.rawValue:
            apartmentsViewState.apartments = apartmentsViewState.apartments.sorted(
                by: { sortAscending ? $0.pricePerNight < $1.pricePerNight : $0.pricePerNight > $1.pricePerNight }
            )
        case FilterOptions.rating.rawValue:
            apartmentsViewState.apartments = apartmentsViewState.apartments.sorted(
                by: { sortAscending ? $0.rating ?? 0 < $1.rating ?? 0 : $0.rating ?? 0 > $1.rating ?? 0 }
            )
        default:
            apartmentsViewState.apartments = apartmentsViewState.apartments.sorted(
                by: { sortAscending ? $0.pricePerNight < $1.pricePerNight : $0.pricePerNight > $1.pricePerNight }
            )
        }
    }
}
