import axios from 'axios'

const http = axios.create({
  baseURL: 'http://localhost:8080/api/v1/'
});

const genericRequest = async ({ method = 'get', resource, id = null, queryParams = {}, token = null, body = {} } = {}) => {
  if (!resource) throw new Error("resource param is missing")

  const url = id ? `${resource}/${id}` : `${resource}/`
  const authHeaders = { "Authorization": `Bearer ${token}` }

  const config = {
    method: method,
    url: url,
    data: body,
  }

  if (queryParams) config.params = queryParams
  if (token) config.headers = authHeaders

  return await http(config)
}

export default {
  get: async ({ resource, id = null, queryParams = {}, token = null } = {}) => {
    return await genericRequest({ method: 'get', resource, id, queryParams, token })
  },
  post: async ({ resource, body = {}, token = null } = {}) => {
    return await genericRequest({ method: 'post', resource, body, token })
  },
  put: async ({ resource, id = null, body = {}, token = null } = {}) => {
    return await genericRequest({ method: 'put', resource, id, body, token })
  },
  delete: async ({ resource, id = null, token = null } = {}) => {
    return await genericRequest({ method: 'delete', resource, id, token })
  }
}
