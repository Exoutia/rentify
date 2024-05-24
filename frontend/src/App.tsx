import Login from '@/Login'
import { RouterProvider, createBrowserRouter } from 'react-router-dom';
import ErrorPage from './error-page';
import Properties from './Properties';
import Root from './Root';
import PostProperty from './PostProperties';

const router = createBrowserRouter([
  {
    path: "/",
    element: <Root />,
    errorElement: <ErrorPage />,
    children: [

      {
        path: "properties/",
        element: <Properties />
      },
      {
        path: "login/",
        element: <Login />
      },
      {
        path: "post-property/",
        element: <PostProperty />
      }
    ]
  },
])

function App() {

  return (
    <RouterProvider router={router} />
  )
}

export default App
