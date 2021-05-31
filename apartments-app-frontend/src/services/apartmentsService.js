import repo from './apiService'

export default {
  createApartment(data, user) {
    return repo.post({ resource: 'apartments', token: user.access_token, body: data })
  },
  updateApartment(data, user, apartmentId) {
    const path = `apartments/${apartmentId}`
    return repo.put({ resource: path, token: user.access_token, body: data })
  },
  getApartment(user, id) {
    return repo.get({ resource: `apartments`, id: id, token: user.access_token })
  },
}
