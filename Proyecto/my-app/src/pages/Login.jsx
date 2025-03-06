import { useState } from 'react'
import './Login.css' // Archivo CSS para estilos personalizados
import Logo from '../components/Logo.jsx'
import axios from 'axios';

const Login = () => {
  const [formData, setFormData] = useState({
    email: '',
    password: ''
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
        const response = await axios.post('http://localhost:8000/login/', formData);
        console.log(response.data);
    } catch (error) {
        console.error(error);
    }
  };

  return (
    <div className="login-container">
      <div className="background-overlay"></div>
      <div className="login-box">
        <Logo />
        <h2 style={{ marginTop: 0 + 'em' }}>Iniciar sesión</h2>
        <form onSubmit={handleSubmit}>
          <div className="input-group">
            <label>Correo electrónico</label>
            <input type="email" placeholder="correo@example.com" onChange={handleChange} required />
          </div>
          <div className="input-group">
            <label>Contraseña</label>
            <input type="password" placeholder="••••••••" onChange={handleChange} required />
          </div>
          <button type="submit" className="login-button">
            Iniciar sesión
          </button>
        </form>
        <p className="register-link">
          ¿No tienes una cuenta? <a href="/register">Regístrate</a>
        </p>
      </div>
    </div>
  )
}

export default Login
