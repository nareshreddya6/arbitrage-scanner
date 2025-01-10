// src/components/ui/card.js

import React from 'react';

export const Card = ({ children, className }) => (
  <div className={`bg-white rounded shadow-md p-4 ${className || ''}`}>{children}</div>
);

export const CardHeader = ({ children }) => <div className="border-b pb-2">{children}</div>;

export const CardTitle = ({ children }) => (
  <h2 className="text-xl font-bold">{children}</h2>
);

export const CardDescription = ({ children }) => (
  <p className="text-sm text-gray-600">{children}</p>
);

export const CardContent = ({ children }) => <div className="mt-4">{children}</div>;
