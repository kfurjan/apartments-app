//
//  PreviewHelpers.swift
//  ApartmentsAppMobile
//
//  Created by Kevin Furjan on 05.06.2021.
//

import Foundation

let loremIpsum = "Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium. "

let apartmentsList = [
    Apartment(
        tile: "Dvosoban apartman",
        city: "Biograd na moru",
        address: "Biogradska 10",
        postalCode: "10000",
        description: String(repeating: loremIpsum, count: 6),
        pricePerNight: 79.99,
        available: true,
        availableFrom: Date.parse("2021-06-15")!,
        availableTo: Date.parse("2021-06-30")!,
        latitude: 17.7,
        longitude: 18.9,
        images: [
            "https://images.wsj.net/im-193186?width=620&size=1.5",
            "https://q-xx.bstatic.com/xdata/images/hotel/840x460/203437766.jpg?k=e111528e2c88d4d692f24f90420d1c6b6b1e4b5c7672f7506a2d39e94e73e006&o=",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSO2z1Q69L_-iwb4zDpSnhuIgVS3PDUtwOP3w&usqp=CAU"
        ],
        rating: 4
    ),
    Apartment(
        tile: "Jednosoban apartman",
        city: "Dubrovnik",
        address: "Dubrovnička 3",
        postalCode: "10000",
        description: String(repeating: loremIpsum, count: 6),
        pricePerNight: 119.99,
        available: false,
        availableFrom: Date.parse("2021-06-15")!,
        availableTo: Date.parse("2021-06-30")!,
        latitude: 17.7,
        longitude: 18.9,
        images: [
            "https://q-xx.bstatic.com/xdata/images/hotel/840x460/203437766.jpg?k=e111528e2c88d4d692f24f90420d1c6b6b1e4b5c7672f7506a2d39e94e73e006&o=",
            "https://images.wsj.net/im-193186?width=620&size=1.5",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSO2z1Q69L_-iwb4zDpSnhuIgVS3PDUtwOP3w&usqp=CAU"
        ],
        rating: 5
    ),
    Apartment(
        tile: "Apartman s pogledom",
        city: "Pula",
        address: "Pulska 9",
        postalCode: "10000",
        description: String(repeating: loremIpsum, count: 6),
        pricePerNight: 99.99,
        available: true,
        availableFrom: Date.parse("2021-06-15")!,
        availableTo: Date.parse("2021-06-30")!,
        latitude: 17.7,
        longitude: 18.9,
        images: [
            "https://q-xx.bstatic.com/xdata/images/hotel/840x460/203437766.jpg?k=e111528e2c88d4d692f24f90420d1c6b6b1e4b5c7672f7506a2d39e94e73e006&o=",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSO2z1Q69L_-iwb4zDpSnhuIgVS3PDUtwOP3w&usqp=CAU",
            "https://images.wsj.net/im-193186?width=620&size=1.5"
        ],
        rating: nil
    )
]
