import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Login from '../pages/Login'
import Register from '../pages/Register'
import RegisterSuccess from '../pages/RegisterSuccess'
import Dashboard from '../pages/Dashboard' // Una nueva página de ejemplo

const AppRouter = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/register" element={<Register />} />
        <Route path="/registerSuccess" element={<RegisterSuccess />} />
      </Routes>
    </Router>
  )
}

export default AppRouter
