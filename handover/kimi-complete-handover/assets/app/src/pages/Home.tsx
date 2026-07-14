import { Button } from '@/components/ui/button';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Separator } from '@/components/ui/separator';
import { Input } from '@/components/ui/input';
import { Progress } from '@/components/ui/progress';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle, DialogTrigger } from '@/components/ui/dialog';
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from '@/components/ui/accordion';
import { ScrollArea } from '@/components/ui/scroll-area';
import { Switch } from '@/components/ui/switch';
import { Label } from '@/components/ui/label';
import { Textarea } from '@/components/ui/textarea';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';
import { Checkbox } from '@/components/ui/checkbox';
import { RadioGroup, RadioGroupItem } from '@/components/ui/radio-group';
import { Slider } from '@/components/ui/slider';
import { Calendar } from '@/components/ui/calendar';
import { Popover, PopoverContent, PopoverTrigger } from '@/components/ui/popover';
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from '@/components/ui/tooltip';
import { format } from 'date-fns';
import { CalendarIcon, ChevronRight, CheckCircle, AlertCircle, TrendingUp, DollarSign, Zap, Globe, ArrowRight, Star } from 'lucide-react';
import { useState } from 'react';
import { cn } from '@/lib/utils';

export default function Home() {
  const [date, setDate] = useState<Date | undefined>(new Date());
  const [email, setEmail] = useState('');
  const [sliderValue, setSliderValue] = useState([50]);

  return (
    <ScrollArea className="h-screen w-full">
      <div className="min-h-screen bg-background text-foreground">
        {/* Header */}
        <header className="border-b bg-card/50 backdrop-blur-sm sticky top-0 z-50">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div className="flex items-center gap-2">
              <div className="w-8 h-8 bg-primary rounded-lg flex items-center justify-center">
                <Zap className="w-5 h-5 text-primary-foreground" />
              </div>
              <span className="text-xl font-bold tracking-tight">AlphaLabs</span>
            </div>
            <nav className="hidden md:flex items-center gap-6">
              <a href="#dashboard" className="text-sm font-medium text-muted-foreground hover:text-foreground transition-colors">Dashboard</a>
              <a href="#analytics" className="text-sm font-medium text-muted-foreground hover:text-foreground transition-colors">Analytics</a>
              <a href="#products" className="text-sm font-medium text-muted-foreground hover:text-foreground transition-colors">Products</a>
              <a href="#settings" className="text-sm font-medium text-muted-foreground hover:text-foreground transition-colors">Settings</a>
            </nav>
            <div className="flex items-center gap-3">
              <Button variant="outline" size="sm">Sign In</Button>
              <Button size="sm">Get Started</Button>
            </div>
          </div>
        </header>

        {/* Hero Section */}
        <section className="relative py-20 lg:py-32 overflow-hidden">
          <div className="absolute inset-0 bg-gradient-to-br from-primary/5 via-transparent to-primary/10" />
          <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="text-center max-w-3xl mx-auto">
              <Badge variant="secondary" className="mb-4 px-3 py-1 text-xs font-medium">
                <Star className="w-3 h-3 mr-1 inline" /> Now with 78 production-grade components
              </Badge>
              <h1 className="text-4xl md:text-6xl font-extrabold tracking-tight mb-6 bg-gradient-to-r from-foreground to-foreground/70 bg-clip-text">
                Build Better Products Faster
              </h1>
              <p className="text-lg md:text-xl text-muted-foreground mb-8 leading-relaxed">
                A comprehensive component library and dashboard system designed for modern SaaS applications. Production-ready, accessible, and beautifully crafted.
              </p>
              <div className="flex flex-col sm:flex-row gap-4 justify-center">
                <Button size="lg" className="gap-2">
                  Start Building <ArrowRight className="w-4 h-4" />
                </Button>
                <Button size="lg" variant="outline">View Documentation</Button>
              </div>
            </div>
          </div>
        </section>

        {/* Stats Overview */}
        <section id="dashboard" className="py-16 border-t">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex items-center justify-between mb-8">
              <div>
                <h2 className="text-3xl font-bold tracking-tight">Dashboard Overview</h2>
                <p className="text-muted-foreground mt-1">Real-time metrics and performance indicators</p>
              </div>
              <div className="flex items-center gap-2">
                <Popover>
                  <PopoverTrigger asChild>
                    <Button variant="outline" className="gap-2">
                      <CalendarIcon className="w-4 h-4" />
                      {date ? format(date, 'PPP') : 'Pick a date'}
                    </Button>
                  </PopoverTrigger>
                  <PopoverContent className="w-auto p-0" align="end">
                    <Calendar mode="single" selected={date} onSelect={setDate} initialFocus />
                  </PopoverContent>
                </Popover>
              </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
              <Card>
                <CardHeader className="flex flex-row items-center justify-between pb-2">
                  <CardTitle className="text-sm font-medium text-muted-foreground">Total Revenue</CardTitle>
                  <DollarSign className="w-4 h-4 text-emerald-500" />
                </CardHeader>
                <CardContent>
                  <div className="text-2xl font-bold">$45,231.89</div>
                  <p className="text-xs text-emerald-500 flex items-center mt-1">
                    <TrendingUp className="w-3 h-3 mr-1" /> +20.1% from last month
                  </p>
                </CardContent>
              </Card>
              <Card>
                <CardHeader className="flex flex-row items-center justify-between pb-2">
                  <CardTitle className="text-sm font-medium text-muted-foreground">Active Users</CardTitle>
                  <Globe className="w-4 h-4 text-blue-500" />
                </CardHeader>
                <CardContent>
                  <div className="text-2xl font-bold">2,350</div>
                  <p className="text-xs text-emerald-500 flex items-center mt-1">
                    <TrendingUp className="w-3 h-3 mr-1" /> +180 new this week
                  </p>
                </CardContent>
              </Card>
              <Card>
                <CardHeader className="flex flex-row items-center justify-between pb-2">
                  <CardTitle className="text-sm font-medium text-muted-foreground">Conversion Rate</CardTitle>
                  <CheckCircle className="w-4 h-4 text-violet-500" />
                </CardHeader>
                <CardContent>
                  <div className="text-2xl font-bold">3.24%</div>
                  <p className="text-xs text-muted-foreground mt-1">Industry avg: 2.8%</p>
                </CardContent>
              </Card>
              <Card>
                <CardHeader className="flex flex-row items-center justify-between pb-2">
                  <CardTitle className="text-sm font-medium text-muted-foreground">Churn Rate</CardTitle>
                  <AlertCircle className="w-4 h-4 text-amber-500" />
                </CardHeader>
                <CardContent>
                  <div className="text-2xl font-bold">0.8%</div>
                  <p className="text-xs text-emerald-500 flex items-center mt-1">
                    <TrendingUp className="w-3 h-3 mr-1" /> -0.2% improvement
                  </p>
                </CardContent>
              </Card>
            </div>

            <Tabs defaultValue="overview" className="w-full">
              <TabsList className="grid w-full grid-cols-3 lg:w-[400px]">
                <TabsTrigger value="overview">Overview</TabsTrigger>
                <TabsTrigger value="analytics">Analytics</TabsTrigger>
                <TabsTrigger value="reports">Reports</TabsTrigger>
              </TabsList>
              <TabsContent value="overview" className="mt-6">
                <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
                  <Card className="lg:col-span-2">
                    <CardHeader>
                      <CardTitle>Performance Overview</CardTitle>
                      <CardDescription>Monthly revenue and user growth over time</CardDescription>
                    </CardHeader>
                    <CardContent>
                      <div className="h-[250px] flex items-end justify-between gap-2">
                        {[40, 65, 45, 80, 55, 90, 70, 85, 60, 95, 75, 88].map((h, i) => (
                          <div key={i} className="flex-1 flex flex-col items-center gap-1">
                            <div className="w-full bg-primary/20 rounded-t-sm relative" style={{ height: `${h}%` }}>
                              <div className="absolute inset-0 bg-primary rounded-t-sm opacity-80" style={{ height: `${Math.min(h * 1.2, 100)}%` }} />
                            </div>
                            <span className="text-[10px] text-muted-foreground">{['J','F','M','A','M','J','J','A','S','O','N','D'][i]}</span>
                          </div>
                        ))}
                      </div>
                    </CardContent>
                  </Card>
                  <Card>
                    <CardHeader>
                      <CardTitle>Quick Actions</CardTitle>
                      <CardDescription>Frequently used operations</CardDescription>
                    </CardHeader>
                    <CardContent className="space-y-3">
                      <Button className="w-full justify-between" variant="outline">
                        Create New Campaign <ChevronRight className="w-4 h-4" />
                      </Button>
                      <Button className="w-full justify-between" variant="outline">
                        Import Data <ChevronRight className="w-4 h-4" />
                      </Button>
                      <Button className="w-full justify-between" variant="outline">
                        Generate Report <ChevronRight className="w-4 h-4" />
                      </Button>
                      <Button className="w-full justify-between" variant="outline">
                        Manage Team <ChevronRight className="w-4 h-4" />
                      </Button>
                    </CardContent>
                  </Card>
                </div>
              </TabsContent>
              <TabsContent value="analytics" className="mt-6">
                <Card>
                  <CardHeader>
                    <CardTitle>Detailed Analytics</CardTitle>
                    <CardDescription>Advanced metrics and user behavior analysis</CardDescription>
                  </CardHeader>
                  <CardContent>
                    <div className="space-y-6">
                      <div>
                        <div className="flex items-center justify-between mb-2">
                          <Label>Processing Capacity</Label>
                          <span className="text-sm text-muted-foreground">{sliderValue[0]}%</span>
                        </div>
                        <Slider value={sliderValue} onValueChange={setSliderValue} max={100} step={1} />
                      </div>
                      <Separator />
                      <div className="grid grid-cols-2 gap-4">
                        <div>
                          <Label className="mb-2 block">Region</Label>
                          <Select>
                            <SelectTrigger>
                              <SelectValue placeholder="Select region" />
                            </SelectTrigger>
                            <SelectContent>
                              <SelectItem value="na">North America</SelectItem>
                              <SelectItem value="eu">Europe</SelectItem>
                              <SelectItem value="ap">Asia Pacific</SelectItem>
                              <SelectItem value="la">Latin America</SelectItem>
                            </SelectContent>
                          </Select>
                        </div>
                        <div>
                          <Label className="mb-2 block">Time Range</Label>
                          <Select defaultValue="30d">
                            <SelectTrigger>
                              <SelectValue placeholder="Select range" />
                            </SelectTrigger>
                            <SelectContent>
                              <SelectItem value="7d">Last 7 days</SelectItem>
                              <SelectItem value="30d">Last 30 days</SelectItem>
                              <SelectItem value="90d">Last 90 days</SelectItem>
                              <SelectItem value="1y">Last year</SelectItem>
                            </SelectContent>
                          </Select>
                        </div>
                      </div>
                    </div>
                  </CardContent>
                </Card>
              </TabsContent>
              <TabsContent value="reports" className="mt-6">
                <Card>
                  <CardHeader>
                    <CardTitle>Generated Reports</CardTitle>
                    <CardDescription>Download or view past reports</CardDescription>
                  </CardHeader>
                  <CardContent>
                    <div className="space-y-4">
                      {['Q1 2026 Revenue Report', 'User Acquisition Analysis', 'Churn Prevention Study', 'Feature Adoption Survey'].map((report, i) => (
                        <div key={i} className="flex items-center justify-between p-3 border rounded-lg hover:bg-muted/50 transition-colors">
                          <div className="flex items-center gap-3">
                            <CheckCircle className="w-5 h-5 text-emerald-500" />
                            <div>
                              <p className="font-medium">{report}</p>
                              <p className="text-sm text-muted-foreground">Generated {format(new Date(2026, 2, 15 - i * 5), 'PP')}</p>
                            </div>
                          </div>
                          <Button variant="ghost" size="sm">Download</Button>
                        </div>
                      ))}
                    </div>
                  </CardContent>
                </Card>
              </TabsContent>
            </Tabs>
          </div>
        </section>

        {/* Products Section */}
        <section id="products" className="py-16 border-t bg-muted/30">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="text-center mb-12">
              <h2 className="text-3xl font-bold tracking-tight">Product Suite</h2>
              <p className="text-muted-foreground mt-2">Everything you need to scale your business</p>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              {[
                { title: 'Starter', price: '$29', desc: 'Perfect for individuals and small projects getting started.', features: ['5 Projects', 'Basic Analytics', 'Community Support', '1GB Storage'] },
                { title: 'Professional', price: '$79', desc: 'For growing teams that need more power and flexibility.', features: ['Unlimited Projects', 'Advanced Analytics', 'Priority Support', '50GB Storage', 'Team Collaboration'], popular: true },
                { title: 'Enterprise', price: '$199', desc: 'Large organizations with advanced security and compliance needs.', features: ['Everything in Pro', 'Custom Integrations', 'Dedicated Account Manager', 'Unlimited Storage', 'SLA Guarantee', 'SSO Authentication'] },
              ].map((plan, i) => (
                <Card key={i} className={cn(plan.popular && 'border-primary shadow-lg ring-1 ring-primary/20')}>
                  {plan.popular && <div className="bg-primary text-primary-foreground text-xs font-semibold py-1 px-3 rounded-t-lg">Most Popular</div>}
                  <CardHeader>
                    <CardTitle>{plan.title}</CardTitle>
                    <CardDescription>{plan.desc}</CardDescription>
                  </CardHeader>
                  <CardContent>
                    <div className="mb-4">
                      <span className="text-4xl font-bold">{plan.price}</span>
                      <span className="text-muted-foreground">/month</span>
                    </div>
                    <ul className="space-y-2 mb-6">
                      {plan.features.map((feature, j) => (
                        <li key={j} className="flex items-center gap-2 text-sm">
                          <CheckCircle className="w-4 h-4 text-emerald-500 flex-shrink-0" />
                          {feature}
                        </li>
                      ))}
                    </ul>
                    <Button className="w-full" variant={plan.popular ? 'default' : 'outline'}>Get Started</Button>
                  </CardContent>
                </Card>
              ))}
            </div>
          </div>
        </section>

        {/* Forms & Feedback Section */}
        <section id="settings" className="py-16 border-t">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
              <div>
                <h2 className="text-3xl font-bold tracking-tight mb-2">Get in Touch</h2>
                <p className="text-muted-foreground mb-6">We'd love to hear from you. Send us a message and we'll respond as soon as possible.</p>
                <div className="space-y-4">
                  <div className="grid grid-cols-2 gap-4">
                    <div className="space-y-2">
                      <Label htmlFor="firstName">First Name</Label>
                      <Input id="firstName" placeholder="John" />
                    </div>
                    <div className="space-y-2">
                      <Label htmlFor="lastName">Last Name</Label>
                      <Input id="lastName" placeholder="Doe" />
                    </div>
                  </div>
                  <div className="space-y-2">
                    <Label htmlFor="email">Email</Label>
                    <Input id="email" type="email" placeholder="john@example.com" value={email} onChange={(e) => setEmail(e.target.value)} />
                  </div>
                  <div className="space-y-2">
                    <Label>Topic</Label>
                    <RadioGroup defaultValue="general">
                      <div className="flex items-center space-x-2">
                        <RadioGroupItem value="general" id="general" />
                        <Label htmlFor="general">General Inquiry</Label>
                      </div>
                      <div className="flex items-center space-x-2">
                        <RadioGroupItem value="support" id="support" />
                        <Label htmlFor="support">Technical Support</Label>
                      </div>
                      <div className="flex items-center space-x-2">
                        <RadioGroupItem value="sales" id="sales" />
                        <Label htmlFor="sales">Sales</Label>
                      </div>
                    </RadioGroup>
                  </div>
                  <div className="space-y-2">
                    <Label htmlFor="message">Message</Label>
                    <Textarea id="message" placeholder="Your message..." rows={4} />
                  </div>
                  <div className="flex items-center gap-2">
                    <Checkbox id="newsletter" />
                    <Label htmlFor="newsletter">Subscribe to our newsletter</Label>
                  </div>
                  <Button className="w-full">Send Message</Button>
                </div>
              </div>

              <div>
                <h3 className="text-xl font-bold mb-4">Frequently Asked Questions</h3>
                <Accordion type="single" collapsible className="w-full">
                  <AccordionItem value="item-1">
                    <AccordionTrigger>What is included in the Starter plan?</AccordionTrigger>
                    <AccordionContent>
                      The Starter plan includes 5 projects, basic analytics, community support, and 1GB of storage. It's perfect for individuals and small projects.
                    </AccordionContent>
                  </AccordionItem>
                  <AccordionItem value="item-2">
                    <AccordionTrigger>Can I upgrade or downgrade my plan?</AccordionTrigger>
                    <AccordionContent>
                      Yes, you can change your plan at any time. When upgrading, you'll be charged the prorated difference. When downgrading, the new rate applies at the next billing cycle.
                    </AccordionContent>
                  </AccordionItem>
                  <AccordionItem value="item-3">
                    <AccordionTrigger>Is there a free trial available?</AccordionTrigger>
                    <AccordionContent>
                      Yes, all plans come with a 14-day free trial. No credit card required to start. You can cancel anytime during the trial period.
                    </AccordionContent>
                  </AccordionItem>
                  <AccordionItem value="item-4">
                    <AccordionTrigger>What payment methods do you accept?</AccordionTrigger>
                    <AccordionContent>
                      We accept all major credit cards (Visa, MasterCard, American Express), PayPal, and bank transfers for annual enterprise plans.
                    </AccordionContent>
                  </AccordionItem>
                  <AccordionItem value="item-5">
                    <AccordionTrigger>How secure is my data?</AccordionTrigger>
                    <AccordionContent>
                      We use industry-standard encryption (AES-256) for data at rest and TLS 1.3 for data in transit. We are SOC 2 Type II certified and GDPR compliant.
                    </AccordionContent>
                  </AccordionItem>
                </Accordion>
              </div>
            </div>
          </div>
        </section>

        {/* Dialog Demo */}
        <section className="py-16 border-t bg-muted/30">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <h2 className="text-3xl font-bold tracking-tight mb-4">Ready to Get Started?</h2>
            <p className="text-muted-foreground mb-8 max-w-2xl mx-auto">
              Join thousands of developers and teams building amazing products with our platform.
            </p>
            <div className="flex gap-4 justify-center">
              <Dialog>
                <DialogTrigger asChild>
                  <Button size="lg">View Demo</Button>
                </DialogTrigger>
                <DialogContent className="sm:max-w-[525px]">
                  <DialogHeader>
                    <DialogTitle>Welcome to AlphaLabs</DialogTitle>
                    <DialogDescription>
                      This is a demonstration of our dialog component. It supports rich content, forms, and interactive elements.
                    </DialogDescription>
                  </DialogHeader>
                  <div className="space-y-4 py-4">
                    <div className="flex items-center gap-4 p-4 border rounded-lg">
                      <div className="w-12 h-12 bg-primary/10 rounded-full flex items-center justify-center">
                        <CheckCircle className="w-6 h-6 text-primary" />
                      </div>
                      <div>
                        <p className="font-medium">Setup Complete</p>
                        <p className="text-sm text-muted-foreground">Your workspace is ready to use</p>
                      </div>
                    </div>
                    <Progress value={75} className="w-full" />
                    <p className="text-sm text-muted-foreground text-center">75% profile completion</p>
                  </div>
                </DialogContent>
              </Dialog>
              <Button size="lg" variant="outline">Learn More</Button>
            </div>
          </div>
        </section>

        {/* Footer */}
        <footer className="border-t py-12 bg-background">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex flex-col md:flex-row justify-between items-center gap-4">
              <div className="flex items-center gap-2">
                <div className="w-6 h-6 bg-primary rounded-md flex items-center justify-center">
                  <Zap className="w-4 h-4 text-primary-foreground" />
                </div>
                <span className="font-semibold">AlphaLabs</span>
              </div>
              <p className="text-sm text-muted-foreground">© 2026 AlphaLabs. All rights reserved.</p>
              <div className="flex gap-4">
                <Button variant="ghost" size="sm">Privacy</Button>
                <Button variant="ghost" size="sm">Terms</Button>
                <Button variant="ghost" size="sm">Contact</Button>
              </div>
            </div>
          </div>
        </footer>
      </div>
    </ScrollArea>
  );
}
