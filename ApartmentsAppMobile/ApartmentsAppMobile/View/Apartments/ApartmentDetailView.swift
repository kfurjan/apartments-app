//
//  ApartmentDetailView.swift
//  ApartmentsAppMobile
//
//  Created by Kevin Furjan on 04.06.2021.
//

import SwiftUI
import SDWebImageSwiftUI

struct StarRatingView: View {
    let rating: Int

    var body: some View {
        HStack {
            ForEach(1...5, id: \.self) { number in
                Image(systemName: number <= self.rating ? startIconFill : starIcon)
                    .foregroundColor(number <= self.rating ? .yellow : .gray)
            }
        }.padding()
    }
}

struct ApartmentDetailView: View {
    let apartment: Apartment

    var body: some View {
        VStack {
            ScrollView(.horizontal, showsIndicators: false) {
                HStack {
                    ForEach(apartment.images, id: \.self) { imageUrl in
                        WebImage(url: URL(string: imageUrl))
                            .resizable()
                            .placeholder {
                                Rectangle().fill(Color.gray)
                            }
                            .indicator(.activity)
                            .transition(.fade(duration: 0.5))
                            .scaledToFill()
                            .frame(minWidth: 0, maxWidth: .infinity, minHeight: 0, maxHeight: 275, alignment: .center)
                            .clipped()
                            .cornerRadius(12)
                    }
                }
            }
            HStack(spacing: 8) { // title
                Text(apartment.title)
                    .font(.title)
                    .fontWeight(.bold)
                    .padding(.horizontal, 5)
                Spacer()
            }

            HStack(spacing: 8) { // city, address
                Image(systemName: locationIconFill)
                    .foregroundColor(Color(secondaryColor))

                Text("\(apartment.city), \(apartment.address)")
                    .font(.headline)

                Spacer()
            }
            .padding(.horizontal, 5)
            .padding(.vertical, 3)

            HStack(spacing: 8) { // price, availability
                Image(systemName: euroSignCircleFill)
                    .foregroundColor(Color(secondaryColor))

                Text("\(String(format: "%.2f", apartment.pricePerNight)) per night")
                    .font(.headline)

                Spacer()

                if apartment.available {
                    Text(available)
                        .font(.headline)
                        .foregroundColor(.green)
                } else {
                    Text(unavailable)
                        .font(.headline)
                        .foregroundColor(.red)
                }
            }
            .padding(.horizontal, 5)
            .padding(.vertical, 3)

            if apartment.rating != nil { // starts
                StarRatingView(rating: apartment.rating!)
            }

            HStack(spacing: 8) { // description
                ScrollView {
                    Text(apartment.apartmentDesc)
                        .font(.subheadline)
                        .multilineTextAlignment(.center)
                }
                .frame(width: .infinity, height: 250, alignment: .center)

            }.padding(.vertical, 10)

            Spacer()
        }
        .background(Color(primaryColor).edgesIgnoringSafeArea(.all))
    }
}

struct ApartmentDetailView_Previews: PreviewProvider {
    static var previews: some View {
        ApartmentDetailView(apartment: apartmentsList[0])
            .preferredColorScheme(.dark)
    }
}
