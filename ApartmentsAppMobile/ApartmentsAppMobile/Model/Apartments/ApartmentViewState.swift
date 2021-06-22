//
//  ApartmentViewState.swift
//  ApartmentsAppMobile
//
//  Created by Kevin Furjan on 22.06.2021.
//

import Foundation

struct ApartmentViewState {
    var sortDescending: Bool
    var isSheetPresented: Bool
    var selectedFilter: String
    var filterOptions: [String]
    var apartments: [Apartment]
}
