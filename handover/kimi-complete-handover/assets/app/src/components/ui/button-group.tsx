import * as React from "react"
import { cva, type VariantProps } from "class-variance-authority"
import { cn } from "@/lib/utils"

const buttonGroupVariants = cva("inline-flex items-center", {
  variants: {
    variant: {
      default: "divide-x divide-border rounded-md border",
      outline: "divide-x divide-border rounded-md border",
      ghost: "divide-x divide-border rounded-md",
    },
    size: {
      default: "",
      sm: "",
      lg: "",
      icon: "",
    },
  },
  defaultVariants: {
    variant: "default",
    size: "default",
  },
})

export interface ButtonGroupProps
  extends React.HTMLAttributes<HTMLDivElement>,
    VariantProps<typeof buttonGroupVariants> {}

function ButtonGroup({ className, variant, size, ...props }: ButtonGroupProps) {
  return (
    <div
      className={cn(buttonGroupVariants({ variant, size }), className)}
      role="group"
      {...props}
    />
  )
}

const ButtonGroupItem = React.forwardRef<
  HTMLButtonElement,
  React.ButtonHTMLAttributes<HTMLButtonElement> & {
    isActive?: boolean
  }
>(({ className, isActive, ...props }, ref) => {
  return (
    <button
      ref={ref}
      className={cn(
        "inline-flex items-center justify-center px-4 py-2 text-sm font-medium transition-colors first:rounded-l-md last:rounded-r-md",
        "hover:bg-muted hover:text-foreground focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring",
        isActive && "bg-muted text-foreground",
        className
      )}
      {...props}
    />
  )
})
ButtonGroupItem.displayName = "ButtonGroupItem"

export { ButtonGroup, ButtonGroupItem, buttonGroupVariants }
