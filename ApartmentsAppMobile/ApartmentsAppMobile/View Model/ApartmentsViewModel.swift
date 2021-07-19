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

    private let _daoRepository = DaoRepositoryFactory.getRepository()
    private let _apiRepository = ApiRepositoryFactory.getRepository()

    @Published var searchBarState = SearchBarState()
    @Published var apartmentsViewState = ApartmentViewState()

    func fetchApartments() {
        _apiRepository.getAllApartments { result in
            switch result {
            case .success(let apartments):
                self._daoRepository.createApartments(apartments: apartments)
                self.apartmentsViewState.apartments = self._daoRepository.retrieveApartments()
            case .failure(_):
                self.apartmentsViewState.apartments = self._daoRepository.retrieveApartments()
            }
        }
    }

    func filterApartments() {
        if searchBarState.text == "" {
            apartmentsViewState.apartments = _daoRepository.retrieveApartments()
        } else {
            apartmentsViewState.apartments = apartmentsViewState.apartments.filter {
                $0.title.lowercased().contains(searchBarState.text.lowercased())
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
