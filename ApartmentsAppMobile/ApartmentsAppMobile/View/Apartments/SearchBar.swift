//
//  Searchbar.swift
//  ApartmentsAppMobile
//
//  Created by Kevin Furjan on 04.06.2021.
//

import SwiftUI

struct SearchBar: View {
    @State private var state = SearchBarState()

    var body: some View {
        HStack {
            TextField(searchPlaceholer, text: $state.text)
                .padding(7)
                .padding(.horizontal, 25)
                .foregroundColor(.white)
                .background(Color(surfaceColor))
                .cornerRadius(8)
                .overlay(
                    HStack {
                        Image(systemName: magnifyingGlass)
                            .foregroundColor(Color(secondaryColor))
                            .frame(minWidth: 0, maxWidth: .infinity, alignment: .leading)
                            .padding(.leading, 8)

                        if state.isLoading {
                            Button(action: {
                                state.text = ""
                            }) {
                                Image(systemName: multiplyCircleFill)
                                    .foregroundColor(Color(secondaryColor))
                                    .padding(.trailing, 8)
                            }
                        }
                    }
                )
                .padding(.horizontal, 10)
                .onTapGesture {
                    state.isLoading = true
                }

            if state.isLoading {
                Button(action: {
                    state.text = ""
                    state.isLoading = false
                    UIApplication.shared.sendAction(#selector(UIResponder.resignFirstResponder), to: nil, from: nil, for: nil)
                }) {
                    Text(cancel)
                        .foregroundColor(Color(secondaryColor))
                }
                .padding(.trailing, 10)
                .transition(.move(edge: .trailing))
                .animation(.easeInOut)
            }
        }
    }
}

struct Searchbar_Previews: PreviewProvider {
    static var previews: some View {
        SearchBar()
            .previewLayout(.sizeThatFits)
            .preferredColorScheme(/*@START_MENU_TOKEN@*/.dark/*@END_MENU_TOKEN@*/)
    }
}
