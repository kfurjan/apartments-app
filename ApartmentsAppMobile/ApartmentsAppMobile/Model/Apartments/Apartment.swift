//
//  Apartment.swift
//  ApartmentsAppMobile
//
//  Created by Kevin Furjan on 04.06.2021.
//

import Foundation

struct Apartment: Identifiable {
    let id = UUID()
    let tile: String
    let city: String
    let address: String
    let postalCode: String
    let description: String
    let pricePerNight: Double
    let available: Bool
    let availableFrom: Date
    let availableTo: Date
    let latitude: Double
    let longitude: Double
    let images: [String]
    let rating: Int?
}
