import React from 'react';
import { Link } from 'react-router-dom'

export const Footer = () => {
    return (
        <footer className="page-footer font-small blue">
            <div className="footer-copyright text-center py-3">© 2020 Copyright:
                 <Link to=""> Products J&L</Link>
            </div>
        </footer>
    );
}