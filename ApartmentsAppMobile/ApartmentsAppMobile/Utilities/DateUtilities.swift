//
//  DateUtilities.swift
//  ApartmentsAppMobile
//
//  Created by Kevin Furjan on 05.06.2021.
//

import Foundation

extension Date {

    /// Create a date from specified parameters
    ///
    /// - Parameters:
    ///   - year: The desired year
    ///   - month: The desired month
    ///   - day: The desired day
    /// - Returns: A `Date` object
    static func from(year: Int, month: Int, day: Int) -> Date? {
        let calendar = Calendar(identifier: .gregorian)
        var dateComponents = DateComponents()
        dateComponents.year = year
        dateComponents.month = month
        dateComponents.day = day
        return calendar.date(from: dateComponents) ?? nil
    }

    /// Create a date from specified parameters
    ///
    /// - Parameters:
    ///   - dateString: The desired date in string
    ///   - dateFormat: The desired format
    /// - Returns: A `Date` object
    static func parse(_ dateString: String, dateFormat: String = "yyyy-MM-dd") -> Date? {
        let dateFormatter = DateFormatter()
        dateFormatter.timeZone = TimeZone.current
        dateFormatter.dateFormat = dateFormat

        return dateFormatter.date(from: dateString) ?? nil
    }
}
