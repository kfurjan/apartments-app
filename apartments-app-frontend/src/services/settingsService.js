import repo from './apiService'

export default {
  createUser(data, user, resource) {
    return repo.post({ resource, token: user.access_token, body: data })
  },
  updateUser(data, user, resource) {
    const path = `${resource}/${user.roleId}`
    return repo.put({ resource: path, token: user.access_token, body: data })
  },
  getSettings(user) {
    return repo.get({ resource: `${user.role}s`, id: user.roleId, token: user.access_token })
  }
}
