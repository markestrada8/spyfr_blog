import { createAuthProvider } from 'react-token-auth'

// TOKENS ARE SET TO EXPIRE IN 15 MINUTES BY DEFAULT AND REFRESH NEEDS TO BE USED
// STORING ACCESS TOKEN IN LOCAL MEMORY WITH QUOTES INCLUDED (?)
export const { useAuth, authFetch, login, logout } = createAuthProvider({
  accessTokenKey: 'access_token',
  onUpdateToken: (token) =>
    fetch('/auth/refresh', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
    })
      .then(response => response.json())
})