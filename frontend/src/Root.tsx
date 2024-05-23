import { Outlet, Link } from "react-router-dom";

export default function Root() {
  return (
    <>
      <header className="sticky top-0 flex h-16 items-center gap-4 border-b bg-background px-4 md:px-6">

        <nav className="hidden flex-col gap-6 text-lg font-medium md:flex md:flex-row md:items-center md:gap-5 md:text-sm lg:gap-6">
          <Link
            to={'login/'}
            className="text-muted-foreground transition-colors hover:text-foreground"
          >
            Login
          </Link>
          <Link
            to={'properties/'}
            className="text-foreground transition-colors hover:text-foreground"
          >
            Properties
          </Link>
        </nav>
      </header>
      <div className="main">
        <Outlet />
      </div>
    </>
  );
}
