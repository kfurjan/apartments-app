//
//  PreviewHelpers.swift
//  ApartmentsAppMobile
//
//  Created by Kevin Furjan on 05.06.2021.
//

import Foundation
import RealmSwift

let loremIpsum = "Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium. "

let apartmentsList = [
    Apartment(
        id: 1,
        title: "Dvosoban apartman",
        city: "Biograd na moru",
        address: "Biogradska 10",
        postalCode: "10000",
        apartmentDesc: String(repeating: loremIpsum, count: 6),
        pricePerNight: 79.99,
        available: true,
        availableFrom: Date.parse("2021-06-15")!,
        availableTo: Date.parse("2021-06-30")!,
        latitude: 17.7,
        longitude: 18.9,
        images: List<String>(),
        rating: 4
    ),
    Apartment(
        id: 2,
        title: "Jednosoban apartman",
        city: "Dubrovnik",
        address: "Dubrovnička 3",
        postalCode: "10000",
        apartmentDesc: String(repeating: loremIpsum, count: 6),
        pricePerNight: 119.99,
        available: false,
        availableFrom: Date.parse("2021-06-15")!,
        availableTo: Date.parse("2021-06-30")!,
        latitude: 17.7,
        longitude: 18.9,
        images: List<String>(),
        rating: 5
    ),
    Apartment(
        id: 3,
        title: "Apartman s pogledom",
        city: "Pula",
        address: "Pulska 9",
        postalCode: "10000",
        apartmentDesc: String(repeating: loremIpsum, count: 6),
        pricePerNight: 99.99,
        available: true,
        availableFrom: Date.parse("2021-06-15")!,
        availableTo: Date.parse("2021-06-30")!,
        latitude: 17.7,
        longitude: 18.9,
        images: List<String>(),
        rating: 2
    )
]
