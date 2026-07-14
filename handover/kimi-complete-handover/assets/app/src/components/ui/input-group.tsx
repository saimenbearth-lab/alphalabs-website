import * as React from "react"
import { cn } from "@/lib/utils"

export interface InputGroupProps extends React.HTMLAttributes<HTMLDivElement> {
  children: React.ReactNode
}

const InputGroup = React.forwardRef<HTMLDivElement, InputGroupProps>(
  ({ className, children, ...props }, ref) => {
    return (
      <div
        ref={ref}
        className={cn("relative flex w-full items-center", className)}
        {...props}
      >
        {children}
      </div>
    )
  }
)
InputGroup.displayName = "InputGroup"

const InputGroupText = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => {
  return (
    <div
      ref={ref}
      className={cn(
        "inline-flex items-center rounded-md border border-input bg-muted px-3 py-2 text-sm text-muted-foreground",
        "first:rounded-r-none first:border-r-0",
        "last:rounded-l-none last:border-l-0",
        "not-first:not-last:hidden",
        className
      )}
      {...props}
    />
  )
})
InputGroupText.displayName = "InputGroupText"

export { InputGroup, InputGroupText }
