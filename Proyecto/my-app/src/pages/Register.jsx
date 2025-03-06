// Register.jsx
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Register.css';
import Logo from '../components/Logo.jsx'
import axios from 'axios';

const Register = () => {
  const [formData, setFormData] = useState({
    firstName: '',
    middleName: '',
    lastName: '',
    secondLastName: '',
    email: '',
    password: '',
    confirmPassword: '',
    dni: '',
    phone: ''
  });

  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (formData.password !== formData.confirmPassword) {
      alert('Las contraseñas no coinciden');
      return;
    }
    try {
      const response = await axios.post('http://localhost:8000/register/', formData);
      console.log(response.data);
      navigate('/registerSuccess');
    } catch (error) {
        console.error(error);
    }
  };

  return (
    <div className="register-container">
      <div className="register-box">
        <Logo />
        <h2>Registrarse</h2>
        <form onSubmit={handleSubmit}>
          <div className="input-group">
            <label>Nombre *</label>
            <input type="text" name="firstName" value={formData.firstName} onChange={handleChange} required />
          </div>
          <div className="input-group">
            <label>Segundo Nombre</label>
            <input type="text" name="middleName" value={formData.middleName} onChange={handleChange} />
          </div>
          <div className="input-group">
            <label>Apellido *</label>
            <input type="text" name="lastName" value={formData.lastName} onChange={handleChange} required />
          </div>
          <div className="input-group">
            <label>Segundo Apellido</label>
            <input type="text" name="secondLastName" value={formData.secondLastName} onChange={handleChange} />
          </div>
          <div className="input-group">
            <label>Correo Electrónico *</label>
            <input type="email" name="email" value={formData.email} onChange={handleChange} required />
          </div>
          <div className="input-group">
            <label>Contraseña *</label>
            <input type="password" name="password" value={formData.password} onChange={handleChange} required />
          </div>
          <div className="input-group">
            <label>Repetir Contraseña *</label>
            <input type="password" name="confirmPassword" value={formData.confirmPassword} onChange={handleChange} required />
          </div>
          <div className="input-group">
            <label>DNI *</label>
            <input type="text" name="dni" value={formData.dni} onChange={handleChange} required />
          </div>
          <div className="input-group">
            <label>Teléfono</label>
            <input type="text" name="phone" value={formData.phone} onChange={handleChange} />
          </div>
          <button type="submit" className="register-button">Registrarse</button>
        </form>
        <p className="terms-text">
          Al registrarte, aceptas los <a href="/terms">Términos de Uso</a> y la <a href="/privacy">Política de Privacidad</a> de ProjecTrack.
        </p>
      </div>
      <div className="background-overlay"></div>
    </div>
  );
};

export default Register;
