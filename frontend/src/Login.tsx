import axios from 'axios';
import React from 'react';
import { useNavigate } from "react-router-dom";

import { Button } from "@/components/ui/button"
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"



const Login: React.FC = () => {

  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const username = e.target[0].value
    const password = e.target[1].value
    try {
      const response = await axios.post('http://localhost:8000/api/token/', {
        username,
        password,
      });
      localStorage.setItem('token', response.data.access);
      localStorage.setItem('refreshToken', response.data.refresh);
      navigate('/properties/');
    } catch (error) {
      console.error('login failed', error);
      return null;
    }
  }
  return (
    <div className="flex justify-center items-center w-[100%] h-[100vh]">
      <form onSubmit={handleSubmit}>
        <Card className="max-w-[350px]">
          <CardHeader>
            <CardTitle>Login Form</CardTitle>
            <CardDescription>Login with your credentials</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="grid w-full items-center gap-4">
              <div className="flex flex-col space-y-1.5">
                <Label htmlFor="username">Username</Label>
                <Input id="username" placeholder="username" />
              </div>
              <div className="flex flex-col space-y-1.5">
                <Label htmlFor="password">Password</Label>
                <Input type="password" id="password" placeholder="Password" />
              </div>
            </div>
          </CardContent>
          <CardFooter>
            <Button type="submit">Submit</Button>
          </CardFooter>
        </Card>
      </form>
    </div>
  );
};

export default Login;
