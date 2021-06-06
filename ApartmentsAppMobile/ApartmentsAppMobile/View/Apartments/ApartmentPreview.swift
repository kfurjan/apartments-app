//
//  ApartmentPreview.swift
//  ApartmentsAppMobile
//
//  Created by Kevin Furjan on 04.06.2021.
//

import SwiftUI
import SDWebImageSwiftUI

struct ApartmentPreview: View {
    let apartment: Apartment

    var body: some View {
        HStack(alignment: .center, spacing: 4) {
            WebImage(url: URL(string: apartment.images.first!))
                .resizable()
                .placeholder {
                    Rectangle().fill(Color.gray)
                }
                .indicator(.activity)
                .transition(.fade(duration: 0.5))
                .scaledToFill()
                .frame(minWidth: 0, maxWidth: 135, minHeight: 0, maxHeight: 135, alignment: .center)
                .clipped()
                .padding(.horizontal, 6)
                .cornerRadius(12)

            VStack(alignment: .leading) {
                Text(apartment.tile)
                    .font(.title3)
                    .fontWeight(.bold)
                    .padding(.vertical, 5)
                    .padding(.horizontal, 2)

                HStack(spacing: 10) {
                    Image(systemName: locationIconFill)
                        .foregroundColor(Color(secondaryColor))
                    Text("\(apartment.city), \(apartment.address)")
                        .font(.headline)
                }
                .padding(.vertical, 2)

                HStack(spacing: 10) {
                    Image(systemName: euroSignCircleFill)
                        .foregroundColor(Color(secondaryColor))
                    Text(apartment.pricePerNight.description)
                        .font(.headline)

                    Spacer()

                    if apartment.available {
                        Image(systemName: checkmark)
                            .foregroundColor(.green)
                            .padding(.horizontal, 15)
                    } else {
                        Image(systemName: xmark)
                            .foregroundColor(.red)
                            .padding(.horizontal, 15)
                    }
                }
                .padding(.vertical, 2)
            }
        }
        .frame(width: UIScreen.main.bounds.width, height: 150, alignment: .center)
        .padding(.horizontal, 5)
        .background(Color(surfaceColor))
        .cornerRadius(16)
    }
}

struct ApartmentPreview_Previews: PreviewProvider {
    static var previews: some View {
        ApartmentPreview(apartment: apartmentsList[0])
            .previewLayout(.sizeThatFits)
            .preferredColorScheme(.dark)
    }
}
