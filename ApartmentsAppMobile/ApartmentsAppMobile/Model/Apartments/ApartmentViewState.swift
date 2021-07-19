//
//  ApartmentViewState.swift
//  ApartmentsAppMobile
//
//  Created by Kevin Furjan on 22.06.2021.
//

import Foundation

struct ApartmentViewState {
    var sortDescending = false
    var isSheetPresented = false
    var selectedFilter = FilterOptions.price.rawValue
    var filterOptions: [String] = FilterOptions.allCases.map { $0.rawValue }
    var apartments: [Apartment] = []
}
