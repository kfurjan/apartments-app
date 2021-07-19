//
//  Apartment.swift
//  ApartmentsAppMobile
//
//  Created by Kevin Furjan on 04.06.2021.
//

import Foundation
import RealmSwift

class Apartment: Object {
    @Persisted var id: Int = 0
    @Persisted var title: String = ""
    @Persisted var city: String = ""
    @Persisted var address: String = ""
    @Persisted var postalCode: String = ""
    @Persisted var apartmentDesc: String = ""
    @Persisted var pricePerNight: Double = 0.0
    @Persisted var available: Bool = false
    @Persisted var availableFrom: Date = Date()
    @Persisted var availableTo: Date = Date()
    @Persisted var latitude: Double = 0.0
    @Persisted var longitude: Double = 0.0
    @Persisted var images: List<String>
    @Persisted var rating: Int?

    convenience init(
        id: Int,
        title: String,
        city: String,
        address: String,
        postalCode: String,
        apartmentDesc: String,
        pricePerNight: Double,
        available: Bool,
        availableFrom: Date,
        availableTo: Date,
        latitude: Double,
        longitude: Double,
        images: List<String>,
        rating: Int? = nil
    ) {
        self.init()
        self.id = id
        self.title = title
        self.city = city
        self.address = address
        self.postalCode = postalCode
        self.apartmentDesc = apartmentDesc
        self.pricePerNight = pricePerNight
        self.available = available
        self.availableFrom = availableFrom
        self.availableTo = availableTo
        self.latitude = latitude
        self.longitude = longitude
        self.images = images
        self.rating = rating
    }
}
