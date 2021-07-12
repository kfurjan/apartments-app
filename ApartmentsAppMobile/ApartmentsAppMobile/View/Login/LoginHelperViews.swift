//
//  LoginHelperViews.swift
//  ApartmentsAppMobile
//
//  Created by Ericsson on 12.07.2021..
//

import SwiftUI

struct ErrorDescriptionView: View {

    let errorMessage: String

    var body: some View {
        HStack {
            Text(errorMessage)
                .foregroundColor(Color(secondaryColor))
        }
        .padding(.horizontal)
        .padding(.top, 30)
    }
}

struct LoginToggleGroup: View {
    @Binding var isGuest: Bool
    @Binding var isRenter: Bool

    var body: some View {
        return HStack {
            VStack {
                Text("Guest")
                Toggle("Guest", isOn: $isGuest).labelsHidden()
            }
            .padding()
            .padding(.horizontal, 5)
            .overlay(
                RoundedRectangle(cornerRadius: 15)
                    .stroke(lineWidth: 0.5)
                    .foregroundColor(isGuest ? Color(secondaryColor) : .gray)
            )

            VStack {
                Text("Renter")
                Toggle("Renter", isOn: $isRenter).labelsHidden()
            }
            .padding()
            .padding(.horizontal, 5)
            .overlay(
                RoundedRectangle(cornerRadius: 15)
                    .stroke(lineWidth: 0.5)
                    .foregroundColor(isRenter ? Color(secondaryColor) : .gray)
            )
        }
        .padding(.horizontal)
        .padding(.top, 15)
        .toggleStyle(SwitchToggleStyle(tint: Color(secondaryColor)))
    }
}
