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

import api from './axiosConfig';



const PostProperty: React.FC = () => {

  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const name = e.target[0].value
    const price = e.target[1].value
    const id = localStorage.getItem('ownerId');

    const data = {
      'name': name,
      'price': price,
      'owner': id
    }
    try {
      api.post('/api/properties/', data)
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
            <CardTitle>Create Property Form</CardTitle>
            <CardDescription>Fill the form to create the property to rent in website</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="grid w-full items-center gap-4">
              <div className="flex flex-col space-y-1.5">
                <Label htmlFor="name">Name</Label>
                <Input id="name" placeholder="Name" />
              </div>
              <div className="flex flex-col space-y-1.5">
                <Label htmlFor="price">Password</Label>
                <Input type="number" id="price" placeholder="100000" />
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

export default PostProperty;
