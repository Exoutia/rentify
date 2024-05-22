import { Outlet } from "react-router-dom";
import { Button } from "./ui/button";

export default function Root() {
  return (
    <>
    <header>
      <nav>
          <Button>Button</Button>
        
          
      </nav>
    </header>
    <div className="main">
      <Outlet />
    </div>
    </>
  );
}
